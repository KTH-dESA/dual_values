# This repository is to collect scripts and experiences with regards to dual values from OSeMOSYS GNU MathProg version

- Add scripts to extract if some one is missing for any of solvers in the /src folder

# Solvers
- GNU MathProg [Will google-group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/kIhri_lnAAAJ?utm_medium=email&utm_source=footer)
To the model file you can add at the end the equation of interest (e.g.):

table ProductionDual
{r in REGION, l in TIMESLICE, f in FUEL, y in YEAR: <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].dual <> 0} <br />
OUT "CSV" <br />
ResultsPath & "/ProductionDual.csv" : <br />
r~REGION, l~TIMESLICE, f~FUEL, y~YEAR, <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].dual~DUAL, <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].lb~LB, <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].ub~UP, <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].val~VALUE, <br />
EBa11_EnergyBalanceEachTS5[r,l,f,y].status~STATUS <br />

- CBC [Vignesh google group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/I_cg4ZM7DQAJ?utm_medium=email&utm_source=footer)
cbc <abc.lp> solve solu <abc_sol.txt> -printing all

- CPLEX [Abhishek and Vignesh scripts](https://groups.google.com/g/osemosys/c/s_pdUdk5q_U/m/pJvdbgRPAgAJ?utm_medium=email&utm_source=footer)
/src are two scripts that are similar to extract the desired dual values

- Gurobi


# Equations that has be used

- s.t. EBb4_EnergyBalanceEachYear4{r in REGION, f in FUEL, y in YEAR}: 
	ProductionAnnual[r,f,y] >= UseAnnual[r,f,y] + sum{rr in REGION} TradeAnnual[r,rr,f,y]*TradeRoute[r,rr,f,y] + AccumulatedAnnualDemand[r,f,y]; [Mark google-group](https://groups.google.com/g/osemosys/c/s_pdUdk5q_U/m/pJvdbgRPAgAJ?utm_medium=email&utm_source=footer)
  This equation **Please add here**
  
  - s.t. EBa11_EnergyBalanceEachTS5{r in REGION, l in TIMESLICE, f in FUEL, y in YEAR}: sum{(m,t) in MODExTECHNOLOGYperFUELout[f]} RateOfActivity[r,l,t,m,y]*OutputActivityRatio[r,t,f,m,y]*YearSplit[l,y] >= SpecifiedAnnualDemand[r,f,y]*SpecifiedDemandProfile[r,f,l,y] + sum{(m,t) in MODExTECHNOLOGYperFUELin[f]} RateOfActivity[r,l,t,m,y]*InputActivityRatio[r,t,f,m,y]*YearSplit[l,y] + sum{rr in REGION} Trade[r,rr,l,f,y]*TradeRoute[r,rr,f,y];
This equation gives the marginal cost of the fuels in each timeslice. This marginal cost takes into account the fixed and variables costs of inputs, capital cost of capacity needed to meet increased demands and emission penalties. [Will google-group](https://groups.google.com/g/osemosys/c/er3k6kaV39o/m/kIhri_lnAAAJ?utm_medium=email&utm_source=footer)

- 
