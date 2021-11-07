# GreenHack 2021: Waste Management 

## Introduction

The waste management chain consists of 2 crucial parts:
- waste collectors, and
- waste processors/recyclers

In the current setup, when a waste collector needs to transfer some waste from point A to point B, 
they need to fill out a form (evidencni list - EVL), which states who is transferring waste, to whom,
and how much waste is being transferred. 

Upon receiving the waste, the waste processors are obliged within a constrained time window to confirm
the received wasted, which is defined with the accompanying EVL.

The described data points are gathered and reported within the `IS-Odpadki` agency [ARSO agency](https://www.arso.gov.si/), 
which is then generating yearly reports on a waste collector and waste processor level. 

## Problem statement

The data within the `IS-Odpadki` system are not always in sync between the waste collectors
and waste processors, as we would expect them to be. The reasons for this are various, 
ranging from a simple typo when filling out the application, through discrepancies in waste measurements, 
up to malicious intent to take advantage of the systems in place.

Such malicious events lead to horrendous outcomes such as recent [dumps](https://www.delo.si/novice/okolje/nezakonito-so-odlozili-vec-kot-500-tisoc-kilogramov-odpadnega-blata/) of waste in the local forests,
which make our environment more toxic and contribute to additional acceleration of climate change, deforestation, and threatening the local animal habitat.


## Solution 

We propose a novel solution to the problem, by implementing an oracle-like system
which is monitoring the reporting of the amounts of waste being transferred in both cases.

The system is able to detect 

### Research 

An official guide on what the waste handling process is like can be found in the following [link](https://www.gov.si/teme/ravnanje-z-odpadki/#e62944).
As a part of the chain are the waste transporters. The list of waste transporters can be found [here](https://www.gov.si/assets/ministrstva/MOP/Dokumenti/Odpadki/Podatki/Prevozniki-odpadkov.pdf).
The waste collectors are another crucial link of the chain, a list of them can be found [here](https://www.gov.si/assets/ministrstva/MOP/Dokumenti/Odpadki/Podatki/Zbiralci-Odpadkov.pdf).
The final link of the chain are the waste processors/recycling points. The official list of approve recyclers is [here](https://www.gov.si/assets/ministrstva/MOP/Dokumenti/Odpadki/Podatki/Predelovalci-odpadkov.pdf).

Additional reports on waste management can be found [here](https://www.gov.si/assets/ministrstva/MOP/Javne-objave/Javne-obravnave/OP-odpadki/op_odpadki.pdf).
Amounts of money invested into waste management can be found [here](https://pxweb.stat.si/SiStatData/pxweb/sl/Data/-/2711809S.px/table/tableViewLayout2/).



## Dashboard (Technical) Details

### Dashboard Demo

## Utilization

We aim at integrating our solution in the existing system - `IS-Odpadki`,
and with that enable the new monitoring feature.

Simple, but very powerful.

## Roadmap

1. First 3 months: Integrate with the existing `IS-Odpadki`
2. First 6 months: Get involved with some of the waste collectors and waste processors
3. First 1 year: set up systems for waste amount estimation
4. First 2 years: A platform to fully manage waste transparently, at the fraction of the cost of sanation of a natural disaster such as a forest waste dump. 

## Call to Action

Join us and use this opportunity to save our habitat, one dumpster at a time.



