# Required Libraries
import rdflib
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS
import re
import requests

# Function to parse installation instructions from README
def parse_installation_instructions(readme_content):
    # Extract installation instructions using regex
    installation_instructions = re.findall(r'(?<=## Installing)(.*?)(?=##)', readme_content, re.DOTALL)
    return installation_instructions

# Function to convert installation instructions to RDF format
def convert_to_rdf(installation_instructions):
    # Create an RDF graph
    g = Graph()

    # Define P-PLAN namespace
    pplan = Namespace("http://purl.org/net/p-plan#")

    # Create RDF triples for installation instructions
    for step in installation_instructions:
        step_uri = URIRef("http://example.org/step/" + re.sub(r'\W+', '', step)[:10])  # Create a unique URI for the step
        g.add((step_uri, RDF.type, pplan.Step))  # Add type triple
        g.add((step_uri, RDFS.label, Literal(step.strip())))  # Add label triple

    return g

# Example usage
readme_url = 'https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/README.md'
readme_content = requests.get(readme_url).text
installation_instructions = parse_installation_instructions(readme_content)
rdf_graph = convert_to_rdf(installation_instructions)

# Save the RDF graph to a file
rdf_graph.serialize(destination='installation_instructions.ttl', format='turtle')