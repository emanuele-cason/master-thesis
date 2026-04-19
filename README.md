<div align="center">
  <img src="presentation/img/logo-unipd.png" alt="University of Padua" height="80">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="presentation/img/logo-dii.png" alt="Department of Industrial Engineering" height="80">

  # Large Eddy Simulation with the Immersed Boundary Method: Implementation of an adaptive Wall-Modeling approach for complex turbulent flows
  
  Master's Degree in Aerospace Engineering — Università degli Studi di Padova
  
  [![Language](https://img.shields.io/badge/Language-English-blue.svg)](#)
  [![Course](https://img.shields.io/badge/Course-Laboratory_of_Computational_Fluid_Dynamics-orange.svg)](#)
  [![Official Publication](https://img.shields.io/badge/Thesis-Padua_Research_Archive-lightgrey.svg)](https://thesis.unipd.it/handle/20.500.12608/106470)
</div>

## Available Materials

- [Thesis Document (PDF)](https://raw.githubusercontent.com/emanuele-cason/master-thesis/main/main.pdf)
- [Presentation (PDF)](https://raw.githubusercontent.com/emanuele-cason/master-thesis/main/presentation/presentation.pdf)
- [Official Publication on Padua Research Archive](https://thesis.unipd.it/handle/20.500.12608/106470)

---

## Abstract

High Reynolds number turbulent flows dominate critical engineering applications, ranging from aircraft and other vehicles to wind turbines and turbomachinery. However, their simulation remains an open challenge: such flows are characterized by a multi-scale nature, requiring an enormous number of degrees of freedom. Wall-Modeled Large Eddy Simulation (WM-LES) addresses this problem by resolving the largest scales of the motion while modeling the smaller ones and the near-wall turbulent structures. 

In the present work, the Immersed Boundary Method (IBM) provides a flexible framework that avoids the complexity of body-fitted meshes. The presence of the immersed geometry is enforced in the discretized governing equations by a forcing algorithm coupled with the wall model. The initial approach for the immersed boundary forcing in the solver was based on the identification of the interface through sign changes of the level set across adjacent cell nodes, resulting in the application of the forcing to a staircase-approximated wall. 

To improve the approach, a refined forcing technique was developed and integrated, based on the analytical computation of the cut-cell wetted area, coupled with a flux redistribution method. This geometric characterization redefines the numerical interface, utilizing the analytically evaluated surface to accurately compute the wall-model forcing, which is then introduced into the governing equations. The result is a more uniform and consistent boundary representation that introduces no significant computational overhead. 

The proposed formulation was tested against two benchmarks: a canonical channel flow, demonstrating good agreement with the analytical Reichardt law, and the ERCOFTAC periodic hills, in which the solver successfully captured complex macroscopic flow topologies, including separation from a curved boundary, the formation of a free shear layer, and flow reattachment. To further assess the robustness of the numerical framework, a highly complex Airbus A320 wing-pylon-engine assembly was simulated under an inoperative engine configuration. The solver proved particularly stable under these demanding conditions, qualitatively reproducing several expected aerodynamic phenomena.

---

## Estratto (Italiano)

I flussi turbolenti ad alto numero di Reynolds dominano applicazioni ingegneristiche critiche, che spaziano dai velivoli e altri veicoli alle turbine eoliche e alle turbomacchine. Tuttavia, la loro simulazione rimane una sfida aperta: tali flussi sono caratterizzati da una natura multi-scala, richiedendo un numero enorme di gradi di libertà. La *Wall-Modeled Large Eddy Simulation* (WM-LES) affronta questo problema risolvendo le scale di moto più grandi e modellando quelle più piccole e le strutture turbolente in prossimità della parete.

Nel presente lavoro, il *Metodo Immersed Boundary* (IBM) fornisce un framework flessibile che evita la complessità delle mesh "body-fitted". La presenza della geometria immersa viene imposta nelle equazioni di governo discretizzate tramite un algoritmo di forzamento accoppiato al modello di parete. L'approccio iniziale per il forzamento del contorno immerso nel solutore si basava sull'identificazione dell'interfaccia attraverso i cambi di segno della funzione *level set* tra nodi cella adiacenti, risultando nell'applicazione del forzamento a una parete approssimata a gradini (*staircase*).

Per migliorare l'approccio, è stata sviluppata e integrata una tecnica di forzamento raffinata, basata sul calcolo analitico dell'area bagnata della *cut-cell*, accoppiata a un metodo di ridistribuzione dei flussi. Questa caratterizzazione geometrica ridefinisce l'interfaccia numerica, utilizzando la superficie valutata analiticamente per calcolare con precisione il forzamento del modello di parete, che viene poi introdotto nelle equazioni di governo. Il risultato è una rappresentazione del contorno più uniforme e coerente che non introduce alcun sovraccarico computazionale significativo.

La formulazione proposta è stata testata su due benchmark: un flusso in canale canonico, dimostrando un buon accordo con la legge analitica di Reichardt, e le colline periodiche ERCOFTAC, in cui il solutore ha catturato con successo complesse topologie di flusso macroscopiche, tra cui la separazione da un contorno curvo, la formazione di un *free shear layer* e il riattacco del flusso. Per valutare ulteriormente la robustezza del framework numerico, è stato simulato un modello altamente complesso, rappresentativo del gruppo ala-pilone-motore di un Airbus A320 in configurazione di motore inoperativo. Il solutore si è dimostrato particolarmente stabile in queste condizioni severe, riproducendo qualitativamente diversi fenomeni aerodinamici attesi.
