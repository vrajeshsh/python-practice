'''To find out the later date out of 2 date inputs'''

print("To find out the later date out of 2 date inputs:")
dd1 = int(input("Enter first date [dd]: "))
mm1 = int(input("Enter first month [mm]: "))
yy1 = int(input("Enter first year [yy]: "))
dd2 = int(input("Enter second date [dd]: "))
mm2 = int(input("Enter second month [mm]: "))
yy2 = int(input("Enter second year [yy]: "))

if yy1 > yy2 or (mm1>mm2 and yy1==yy2) or (dd1>dd2 and mm1==mm2 and yy1==yy2):
	ans = "First"
elif yy1 < yy2 or (mm1<mm2 and yy1==yy2) or (dd1<dd2 and mm1==mm2 and yy1==yy2):
	ans = "Second"
else:
	ans="Equal"

print("\nFirst Date\t\t\tSecond Date\t\t\tGreater\n"
	,dd1,"-",mm1,"-",yy1,"\t\t\t",dd2,"-",mm2,"-",yy2,"\t\t\t",ans,sep='')
