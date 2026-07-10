---
name: ontology-driven-cps-dataspace
version: 1.0.0
description: Ontology-driven dataspace approach for reproducible test annotation in Cyber-Physical Energy Systems using three-viewpoint ontology framework (HTD-O, SCM-O, OPMW).
category: systems-engineering
tags: [cyber-physical systems, ontology, reproducibility, dataspace, energy systems, test annotation, provenance, SysML]
source: arXiv:2604.19686v1
authors: [Kai Heussen, et al.]
date: 2026-04-21
---

# Ontology-Driven Dataspace for Reproducible CPS Energy Systems Testing

## Overview

A **three-viewpoint ontology framework** for reproducible test annotation in Cyber-Physical Energy Systems (CPES). Uses dataspaces to enable cross-laboratory test reproduction, standardized metadata capture, and full provenance tracking. Demonstrated via PV inverter testing across Irish and Swiss laboratories.

## Three-Viewpoint Ontology Architecture

```
┌─────────────────────────────────────────────────────┐
│                  DATASPACE LAYER                     │
│         (RDF/OWL descriptions, SPARQL queries)       │
├───────────────┬───────────────┬─────────────────────┤
│    HTD-O      │    SCM-O      │       OPMW          │
│  (Testing     │  (System      │    (Workflow &      │
│   Domain)     │   Config)     │    Provenance)      │
├───────────────┼───────────────┼─────────────────────┤
│ Test types    │ Components    │ Workflow spec        │
│ Test steps    │ Connections   │ Execution log        │
│ Acceptance    │ Topology      │ Data lineage         │
│ criteria      │ Parameters    │ Provenance chain     │
└───────────────┴───────────────┴─────────────────────┘
```

### Viewpoint 1: HTD-O (Holistic Test Description Ontology)

**Purpose**: Describe WHAT is being tested and HOW.

- Aligned with **EXPO** (Experiment Ontology)
- Key concepts:
  - `TestObjective` — what the test aims to verify
  - `TestProcedure` — sequence of test steps
  - `TestInput` — stimuli applied to system under test
  - `ExpectedOutcome` — acceptance criteria
  - `ActualOutcome` — measured results

```python
class HTDontology:
    """Holistic Test Description Ontology entities."""
    
    NAMESPACE = "http://ontology.cps-energy.org/htd#"
    
    CLASSES = [
        "TestObjective",
        "TestProcedure", 
        "TestStep",
        "TestInput",
        "ExpectedOutcome",
        "ActualOutcome",
        "EquipmentUnderTest",
        "TestEnvironment"
    ]
    
    PROPERTIES = [
        "hasObjective",
        "hasProcedure",
        "hasStep",
        "hasInput",
        "hasExpectedOutcome",
        "hasActualOutcome",
        "testsEquipment",
        "inEnvironment"
    ]
```

### Viewpoint 2: SCM-O (System Configuration Model Ontology)

**Purpose**: Describe the SYSTEM under test (topology + parameters).

- Lightweight topology-oriented modeling
- Aligns with: **CIM** (Common Information Model), **IEC 61850-6 SCL**, **SysML**, **SEAS**, **SAREF4SYST**
- Key concepts:
  - `Component` — physical or digital entity
  - `Connection` — links between components
  - `Parameter` — configurable values
  - `Topology` — overall system structure

```python
class SCMOntology:
    """System Configuration Model Ontology entities."""
    
    NAMESPACE = "http://ontology.cps-energy.org/scm#"
    
    CLASSES = [
        "Component",
        "Connection", 
        "Parameter",
        "Topology",
        "ElectricalComponent",
        "ControlSystem",
        "Sensor",
        "Actuator"
    ]
    
    # Aligns with IEC 61850-6 SCL for substation configuration
    # Aligns with CIM for power system modeling
    # Aligns with SysML for systems engineering
```

### Viewpoint 3: OPMW (Ontology for Planning and Managing Workflows)

**Purpose**: Track HOW the test was executed (provenance).

- Extends **W3C PROV-O** standard
- Separates **workflow specification** from **workflow execution**
- Key concepts:
  - `WorkflowTemplate` — planned process
  - `WorkflowExecution` — actual execution record
  - `DataProduct` — input/output data with lineage
  - `StepExecution` — individual step record with timestamps

```python
class OPMWOntology:
    """Workflow and Provenance Ontology entities."""
    
    NAMESPACE = "http://ontology.cps-energy.org/opmw#"
    
    CLASSES = [
        "WorkflowTemplate",
        "WorkflowExecution",
        "DataProduct",
        "StepExecution",
        "Agent",
        "Activity"
    ]
    
    # Extends W3C PROV-O
    # Key: separation of specification vs execution
```

## Dataspace Implementation Pattern

### Step 1: Annotate Test with Ontologies

```python
from rdflib import Graph, Namespace, Literal, RDF

HTD = Namespace("http://ontology.cps-energy.org/htd#")
SCM = Namespace("http://ontology.cps-energy.org/scm#")
OPMW = Namespace("http://ontology.cps-energy.org/opmw#")

def annotate_test(test_config, system_config, execution_log):
    g = Graph()
    g.bind("htd", HTD)
    g.bind("scm", SCM)
    g.bind("opmw", OPMW)
    
    # Add test description (HTD-O)
    test_uri = URIRef(f"urn:test:{test_config['id']}")
    g.add((test_uri, RDF.type, HTD.TestProcedure))
    for step in test_config['steps']:
        step_uri = URIRef(f"urn:step:{step['id']}")
        g.add((test_uri, HTD.hasStep, step_uri))
        g.add((step_uri, RDF.type, HTD.TestStep))
    
    # Add system configuration (SCM-O)
    system_uri = URIRef(f"urn:system:{system_config['id']}")
    g.add((system_uri, RDF.type, SCM.Topology))
    for comp in system_config['components']:
        comp_uri = URIRef(f"urn:component:{comp['id']}")
        g.add((system_uri, SCM.hasComponent, comp_uri))
    
    # Add execution provenance (OPMW)
    exec_uri = URIRef(f"urn:execution:{execution_log['id']}")
    g.add((exec_uri, RDF.type, OPMW.WorkflowExecution))
    g.add((exec_uri, OPMW.realizes, test_uri))
    
    return g
```

### Step 2: Publish to Dataspace

```python
def publish_to_dataspace(graph, dataspace_endpoint):
    """Publish annotated test description to dataspace."""
    serialized = graph.serialize(format="turtle")
    # POST to dataspace endpoint
    response = requests.post(
        f"{dataspace_endpoint}/publish",
        data=serialized,
        headers={"Content-Type": "text/turtle"}
    )
    return response.status_code == 200
```

### Step 3: Cross-Laboratory Reproduction Query

```python
def find_reproducible_tests(dataspace_endpoint, test_type):
    """Query dataspace for tests that can be reproduced."""
    query = f"""
    PREFIX htd: <http://ontology.cps-energy.org/htd#>
    PREFIX scm: <http://ontology.cps-energy.org/scm#>
    PREFIX opmw: <http://ontology.cps-energy.org/opmw#>
    
    SELECT ?test ?system ?execution ?lab
    WHERE {{
        ?test a htd:TestProcedure ;
              htd:hasObjective ?obj .
        ?obj a htd:{test_type} .
        ?execution opmw:realizes ?test ;
                   opmw:executedBy ?lab .
        ?system scm:usedIn ?test .
    }}
    """
    # Execute SPARQL query against dataspace
    return execute_sparql(dataspace_endpoint, query)
```

## Cross-Laboratory Reproduction Methodology

### Identified Reproduction Gaps (UCD Ireland ↔ ZHAW Switzerland)

1. **Impedance characterization**: Grid simulator impedance differs between labs
2. **Metadata capture**: Inconsistent recording of environmental conditions
3. **Event logging**: Timestamp synchronization and event annotation vary
4. **Parameter mapping**: Different naming conventions for equivalent parameters

### Resolution Strategy

```
Lab A Test → HTD-O/SCM-O/OPMW annotation → Dataspace publication
                                                    ↓
Lab B Query → Retrieve full test specification → SCM-O system mapping
                                                    ↓
Lab B Execute → OPMW provenance tracking → Compare results
```

## Application Domains

- Power electronics testing (PV inverters, wind turbines)
- Smart grid equipment certification
- EV charging system compliance testing
- Building energy management system verification
- Any CPS domain requiring reproducible testing

## Key Benefits

1. **Reproducibility**: Full provenance chain from test specification to execution
2. **Interoperability**: Ontology alignment with CIM, IEC 61850, SysML, PROV-O
3. **Scalability**: Dataspace pattern supports federated, decentralized test databases
4. **Traceability**: Every test result traceable to specific equipment, configuration, and conditions

## Pitfalls & Caveats

1. **Ontology alignment effort**: Mapping between HTD-O/SCM-O and domain standards requires expertise
2. **Metadata overhead**: Comprehensive annotation is time-consuming; automate where possible
3. **Dataspace maturity**: Dataspace pattern is relatively new; tooling still evolving
4. **Cross-lab calibration**: Even with perfect annotations, physical differences require careful interpretation
5. **Scalability of RDF**: Large test datasets may require triple store optimization

## References

- arXiv:2604.19686v1 — Towards Reproducible Test Annotation for Cyber-Physical Energy Systems using Ontology-driven Dataspaces (Heussen et al., 2026)
- OSMSES 2026 conference paper
- Zenodo dataset: doi:10.5281/zenodo.18868542
- Related: W3C PROV-O, IEC 61850-6, CIM (IEC 61970), SysML
