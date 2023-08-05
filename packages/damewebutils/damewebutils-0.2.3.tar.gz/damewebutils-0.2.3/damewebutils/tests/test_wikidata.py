#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damewebutils; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from unittest import TestCase
from SPARQLWrapper import SPARQLWrapper, JSON
import requests


class TestWikidata(TestCase):

    def test_dbpedia_asturias(self):
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        l1 = []
        for result in results["results"]["bindings"]:
            l1.append(result["label"]["value"])
        self.assertEqual(l1[0], 'Asturias')

    def test_surnames(self):
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?surname ?surnameLabel ?count
WHERE
{
  {
    SELECT ?surname (COUNT(?human) AS ?count) WHERE {
    # ?human wdt:P31 wd:Q5.
      ?human wdt:P734 ?surname.
    }
    GROUP BY ?surname ORDER BY DESC(?count) LIMIT 2
  }
  SERVICE wikibase:label
  { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
LIMIT 2
# limit to 10 results so we don't timeout
"""
        r = requests.get(url, params={'format': 'json', 'query': query})
        data = r.json()
        l1 = []
        for result in data["results"]["bindings"]:
            elem = [result['surnameLabel']['value'], result['count']['value']]
            l1.append(elem[0])
        self.assertEqual(l1, ['Li', 'Wang'])

    def test_openstreetmap(self):
        # https://www.wikidata.org/wiki/Wikidata:OpenStreetMap
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?itemLabel ?item ?OSM ?code
WHERE
{
        ?item wdt:P31 wd:Q6465 . #French départements
        ?item wdt:P300 ?code . #with ISO 3166-2 code
        OPTIONAL { ?item wdt:P402 ?OSM }. #OSM relation if available
        SERVICE wikibase:label { bd:serviceParam wikibase:language "fr" }
}
"""
        dicc1 = {'format': 'json', 'query': query}
        r = requests.get(url, params=dicc1)
        data = r.json()
        l1 = []
        vector = data['results']['bindings'][0]
        values = [vector['code']['value'],
                  vector['OSM']['value'],
                  vector['itemLabel']['value'],
                  vector['item']['value']]
        arr1 = ['FR-44', '7432', 'Loire-Atlantique',
                'http://www.wikidata.org/entity/Q3068']
        self.assertEqual(values, arr1)

    def test_conan_doyle(self):
        # https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial#Arthur_Conan_Doyle_books
        url = 'https://query.wikidata.org/sparql'
        query = """
        SELECT ?book ?bookLabel
        WHERE
        {
        ?book wdt:P50 wd:Q35610.
        SERVICE wikibase:label
        { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
        }
        ORDER BY DESC(?book)
        LIMIT 2
        """
        dicc = {'format': 'json', 'query': query}
        r = requests.get(url, params=dicc)
        data = r.json()
#        print(data['results']['bindings'][0]['bookLabel'])
        arr1 = data['results']['bindings'][0]['bookLabel']
        dicc1 = {'type': 'literal', 'value': 'Q45192'}
        self.assertEqual(arr1, dicc1)

    def test_ue(self):
        # https://towardsdatascience.com/a-brief-introduction-to-wikidata-bb4e66395eb1
        url = 'https://query.wikidata.org/sparql'
        query = """
        SELECT ?country ?countryLabel ?capitalLabel ?population
        WHERE
        {
        ?country wdt:P463 wd:Q458.
        ?country wdt:P36 ?capital.
        ?capital wdt:P1082 ?population.
        SERVICE wikibase:label
        { bd:serviceParam wikibase:language " [AUTO_LANGUAGE],en". }
        }
        ORDER BY DESC(?capital)
        """
        dicc1 = {'format': 'json', 'query': query}
        r = requests.get(url, params=dicc1)
        data = r.json()
        arr1 = data['results']['bindings'][0]['countryLabel']['value']
        val1 = "Kingdom of the Netherlands"
        self.assertEqual(arr1, val1)

    def test_cervantes(self):
        # http://www.cervantesvirtual.com/obra/la-serrana-de-la-vera--0/
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?workLabel WHERE {
 wd:Q165257 wdt:P2799 ?id
 BIND(uri(concat("http://data.cervantesvirtual.com/person/", ?id)) as ?bvmcID)
 SERVICE <http://data.cervantesvirtual.com/openrdf-sesame/repositories/data> {
 ?bvmcID <http://rdaregistry.info/Elements/a/authorOf> ?work .
 ?work rdfs:label ?workLabel
 }
}
ORDER BY (?id)
"""
        dicc = {'format': 'json', 'query': query}
        r = requests.get(url, params=dicc)
        data = r.json()
        arr1 = data['results']['bindings'][0]
        dicc2 = {'workLabel': {'type': 'literal',
                               'value': 'El príncipe inocente : comedia'}}
        self.assertEqual(arr1, dicc2)

    def test_number_of_computer_types(self):
        url = 'https://query.wikidata.org/sparql'
        query = """
        SELECT (count(*) as ?instances) WHERE  {
            # Instance has a type of home computers
            ?instance wdt:P31 wd:Q473708
        }
"""
        dicc = {'format': 'json', 'query': query}
        r = requests.get(url, params=dicc)
        data = r.json()
        print(data['results']['bindings'])
        val = int(data['results']['bindings'][0]['instances']['value'])
        self.assertTrue(val > 80)
