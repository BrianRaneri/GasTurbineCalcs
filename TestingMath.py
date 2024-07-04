from math import sqrt



def inletAreaCalc(mDot,M,T_0,P_0,gamma):

    exp = (gamma+1)/(2*(gamma-1))
    inletArea = mDot * sqrt(T_0) / (P_0 * M) * sqrt(287/gamma)*((1+(gamma-1)/2 * (M*M)))**exp
    return inletArea


print(inletAreaCalc(91.497,0.8,298,101325,1.4))
