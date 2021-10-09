# Proyecto1-Opti
### Problema de Programacion Lineal: Transporte
### Solver Elegido: LPSolve
### Python 3.9.6
## balanced_inputs
Todos los inputs que van a ser ingresados para generar casos balanceados aleatorios.

## balanced_instances
Todas las instancias balanceadas generadas para ser resueltas en LPSolve.

## not_balanced_inputs
Todos los inputs que van a ser ingresados para generar casos no balanceados aleatorios.

## not_balanced_instances
Todas las instancias no balanceadas generadas para ser resueltas en LPSolve.

## Makefile
Archivo makefile que permite ejecutar todos los inputs para cada caso del problema:
#### balanced
Ejecuta todos los inputs de casos balanceados y genera los archivos para LPSolve
#### not_balanced
Ejecuta todos los inputs de casos no balanceados y genera los archivos para LPSolve

## solverLP.py
Programa en Python que genera las instancias para resolver en LPSolve, recibe como inputs los parametros necesarios para generar las instancias, devolviendo un archivo .lp
