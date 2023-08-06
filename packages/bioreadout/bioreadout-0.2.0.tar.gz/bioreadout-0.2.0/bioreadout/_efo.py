from functools import cached_property

import pandas as pd
from bionty import EntityTable, Ontology
from bionty._settings import check_datasetdir_exists, settings

EFO_DF_D3 = "https://bionty-assets.s3.amazonaws.com/efo_df.json"


class EFO(EntityTable):
    """Experimental Factor Ontology.

    https://www.ebi.ac.uk/ols/ontologies/efo
    """

    def __init__(self, id=None, reload=False) -> None:
        super().__init__(id=id)
        self._reload = reload
        self._filepath = settings.datasetdir / "efo_df.json"
        self._prefix = "http://www.ebi.ac.uk/efo/"
        self._readout_terms = {
            "assay": "OBI:0000070",
            "assay_by_molecule": "EFO:0002772",
            "assay_by_instrument": "EFO:0002773",
            "assay_by_sequencer": "EFO:0003740",
            "measurement": "EFO:0001444",
        }

    @cached_property
    def df(self) -> pd.DataFrame:
        """DataFrame."""
        if not self._filepath.exists():
            self._download_df()
        df = pd.read_json(self._filepath)
        df.index.name = "id"
        return df

    @cached_property
    def ontology(self):
        """Cell ontology."""
        url = "http://www.ebi.ac.uk/efo/efo.owl"
        localpath = settings.dynamicdir / "efo.obo"
        url = url if ((not localpath.exists()) or (self._reload)) else None
        ontology_ = Ontology(handle=localpath, url=url, prefix=self._prefix)
        if url is not None:
            ontology_.write_obo()
        return ontology_

    @cached_property
    def assay(self):
        """Assays OBI:0000070."""
        return self.ontology._list_subclasses(self._readout_terms["assay"])

    @cached_property
    def assay_by_molecule(self):
        """Assays by molecule EFO:0002772."""
        return self.ontology._list_subclasses(self._readout_terms["assay_by_molecule"])

    @cached_property
    def assay_by_instrument(self):
        """Assays by instrument EFO:0002773."""
        return self.ontology._list_subclasses(
            self._readout_terms["assay_by_instrument"]
        )

    @cached_property
    def assay_by_sequencer(self):
        """Assay by sequencer EFO:0003740."""
        return self.ontology._list_subclasses(self._readout_terms["assay_by_sequencer"])

    @cached_property
    def measurement(self):
        """Measurement EFO:0001444."""
        return self.ontology._list_subclasses(self._readout_terms["measurement"])

    def _create_df_from_ontology(self) -> pd.DataFrame:
        return pd.DataFrame(
            [
                (term.id.replace(self._prefix, "").replace("_", ":"), term.name)
                for term in self.ontology.terms()
                if term.id.startswith(("EFO:", self._prefix))
            ],
            columns=["id", "name"],
        ).set_index("id")

    @check_datasetdir_exists
    def _download_df(self):
        from urllib.request import urlretrieve

        urlretrieve(
            EFO_DF_D3,
            self._filepath,
        )

    def parse_readout(self, term_id):
        """Parse readout attributes from EFO."""

        def _list_to_str(lst: list):
            if len(lst) == 0:
                return None
            elif len(lst) == 1:
                return lst[0].name  # type: ignore
            else:
                return ";".join([i.name for i in lst])

        term = self.ontology.get_term(term_id)
        superclasses = term.superclasses()

        # get the molecule term
        molecules = [i for i in self.assay_by_molecule if i in superclasses]
        # get the instrument term
        instruments = [i for i in self.assay_by_sequencer if i in superclasses]
        if len(instruments) == 0:
            instruments = [i for i in self.assay_by_instrument if i in superclasses]
        # get the measurement for non-molecular readouts
        measurements = [i for i in self.measurement if i in superclasses]

        readout = {
            "efo_id": term_id,
            "name": term.name,
            "molecule": _list_to_str(molecules),
            "instrument": _list_to_str(instruments),
            "measurement": _list_to_str(measurements),
        }

        return readout


def readout(efo_id: str):
    """Get readout attributes from EFO id."""
    return EFO().parse_readout(term_id=efo_id)
