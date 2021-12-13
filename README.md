# This repository is to collect scripts and experiences with regards to dual values from OSeMOSYS GNU MathProg version

Add scripts to extract if some one is missing for any of solvers in the /src folder

## Solvers
### GNU MathProg [Will OSeMOSYS google group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/kIhri_lnAAAJ?utm_medium=email&utm_source=footer)
To the model file you can add at the end the equation of interest (e.g.):

<pre><code>table ProductionDual
{r in REGION, l in TIMESLICE, f in FUEL, y in YEAR:
EBa11_EnergyBalanceEachTS5[r,l,f,y].dual <> 0}
OUT "CSV"
ResultsPath & "/ProductionDual.csv" : 
r~REGION, l~TIMESLICE, f~FUEL, y~YEAR, 
EBa11_EnergyBalanceEachTS5[r,l,f,y].dual~DUAL, 
EBa11_EnergyBalanceEachTS5[r,l,f,y].lb~LB,
EBa11_EnergyBalanceEachTS5[r,l,f,y].ub~UP,
EBa11_EnergyBalanceEachTS5[r,l,f,y].val~VALUE,
EBa11_EnergyBalanceEachTS5[r,l,f,y].status~STATUS </code></pre>

### CBC [Vignesh OSeMOSYS google group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/I_cg4ZM7DQAJ?utm_medium=email&utm_source=footer)
cbc <abc.lp> solve solu <abc_sol.txt> -printing all

### CPLEX [Abhishek and Vignesh scripts](https://groups.google.com/g/osemosys/c/s_pdUdk5q_U/m/pJvdbgRPAgAJ?utm_medium=email&utm_source=footer)
/src are two scripts that are similar to extract the desired dual values

### Gurobi
**please add here**

## Equations that has be used

- s.t. EBb4_EnergyBalanceEachYear4{r in REGION, f in FUEL, y in YEAR}: 
	ProductionAnnual[r,f,y] >= UseAnnual[r,f,y] + sum{rr in REGION} TradeAnnual[r,rr,f,y]*TradeRoute[r,rr,f,y] + AccumulatedAnnualDemand[r,f,y]; [Mark OSeMOSYS google group](https://groups.google.com/g/osemosys/c/s_pdUdk5q_U/m/pJvdbgRPAgAJ?utm_medium=email&utm_source=footer)
  This equation **Please add here**
  
- s.t. EBa11_EnergyBalanceEachTS5{r in REGION, l in TIMESLICE, f in FUEL, y in YEAR}: sum{(m,t) in MODExTECHNOLOGYperFUELout[f]} RateOfActivity[r,l,t,m,y]*OutputActivityRatio[r,t,f,m,y]*YearSplit[l,y] >= SpecifiedAnnualDemand[r,f,y]*SpecifiedDemandProfile[r,f,l,y] + sum{(m,t) in MODExTECHNOLOGYperFUELin[f]} RateOfActivity[r,l,t,m,y]*InputActivityRatio[r,t,f,m,y]*YearSplit[l,y] + sum{rr in REGION} Trade[r,rr,l,f,y]*TradeRoute[r,rr,f,y];
This equation gives the marginal cost of the fuels in each timeslice. This marginal cost takes into account the fixed and variables costs of inputs, capital cost of capacity needed to meet increased demands and emission penalties. [Will OSeMOSYS google group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/kIhri_lnAAAJ?utm_medium=email&utm_source=footer)

- s.t. E8_AnnualEmissionsLimit{r in REGION, e in EMISSION, y in YEAR: AnnualEmissionLimit[r,e,y] <> -1}: sum{l in TIMESLICE, (m,t) in MODExTECHNOLOGYperEMISSION[e]} EmissionActivityRatio[r,t,e,m,y]*RateOfActivity[r,l,t,m,y]*YearSplit[l,y]+AnnualExogenousEmission[r,e,y] <= AnnualEmissionLimit[r,e,y];
[Georgios and Hauke OSeMOSYS google group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/fsqdLxHfBAAJ?utm_medium=email&utm_source=footer)
Cost of one more emission unit
