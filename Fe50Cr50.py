MaterialExchange={
            "FeCr-FeCr"   :0.029
            }
RKKYExchange={
            "FeCr2-FeCr1"  :-0.0008,
            "FeCr1-FeCr2"  :-0.0008
            }

FeCr_Parameters={
            "MaterialThickness":            (50.0,   ),
            "MLThickness":                  (0.15,  ),
            "ZeemanThickness":              (1.0,   ),
            "MaterialName":                 ("FeCr",),
            "MaterialS":                    (1,     ),
            "MaterialExtraField":           (0,     ),
            "MaterialExtraFieldDirection":  (0,     ),
            "MaterialSaturationM":          (778.5, ),
            "CurieTemperature":             (0,     ),
            "GammaCoefficient":             (0.86,  ),
            "InitPosition":                 (0.0,   ),
            "InitB":                        (1.0,   ),
            "LongRangeInteractionLength":   (0.0,   ),
            "LongRangeExchangeFlag":         False,
            "InitPositionSingle":            0,
            "PeriodicBoundaryConditions":    False
            }


from CalculationClass import simulation, timeit
from viewer import reader
# ctrl+shift+P: Debug Visualizer: New View

@timeit
def f(PathToFolder,StructureParameters,StructureExchange,LongRangeExchange):
    Hmin=0.0
    Hmax=1.000
    Hsteps=2
    Tmin=1
    Tmax=450
    Tsteps=128
    S=simulation(DeleteFlag=True,
                 DescendingCoefficient=2,
                 PathToFolder=PathToFolder,
                 StructureParameters=StructureParameters,
                 StructureExchange=StructureExchange,
                 LongRangeExchange=LongRangeExchange,
                 NumberOfIterationM=50,
                 NumberOfIterationTheta=1,
                 NumberOfSteps=1000)
    S.mode(Debug=False)
    file=S.GetMHvsT(
                    Hmin=Hmin,
                    Hmax=Hmax,
                    Hsteps=Hsteps,
                    Tmin=Tmin,
                    Tmax=Tmax,
                    Tsteps=Tsteps,
                    FieldDirection=0)
    data=reader(file)
    data.GetMHonT()
    data.GetMTonH()

f(PathToFolder="Fe50Cr50 50.0 nm J=0.029 M=778.5",StructureParameters=FeCr_Parameters,StructureExchange=MaterialExchange,LongRangeExchange=RKKYExchange)
