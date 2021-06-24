database = open("WPP2019_POP_F07_1_POPULATION_BY_AGE_BOTH_SEXES_to_CSV_2020only.csv", "r")
database2_deaths = open("owid-covid-data-20210618_featuresremoved.csv", "r")


offset = 0 #jump first line
FV = []
CFR_base = 0.0139

cfr_base = []
cfr_base.append("CFR")
cfr_base.append(0) # 0-9
cfr_base.append(0) # 10-19
cfr_base.append(0.0002) # 20-29
cfr_base.append(0.0005) # 30-39
cfr_base.append(0.001) # 40-49
cfr_base.append(0.003) # 50-59
cfr_base.append(0.0127) # 60-69
cfr_base.append(0.064) # 70-79
cfr_base.append(0.2048) # 80+
  
pop_base = []
pop_base.append("Coreia")
pop_base.append(4153813.0) # 0-9
pop_base.append(4753258.0) # 10-19
pop_base.append(6716294.0) # 20-29
pop_base.append(7079839.0) # 30-39
pop_base.append(8218844.0) # 40-49
pop_base.append(8476699.0) # 50-59
pop_base.append(6453706.0) # 60-69
pop_base.append(3560646.0) # 70-79
pop_base.append(1856084.0) # 80+

for line_file in database:
  if(offset == 0):
	offset = offset + 1
	continue
  
  line_file = line_file.split(";")
  line_file = [y.replace(',','.').replace('\n','') for y in line_file]
  
  country = []
  
  country.append(line_file[0])
  country.append((float(line_file[1])+float(line_file[2]))*1000) # 0-9
  country.append((float(line_file[3])+float(line_file[4]))*1000) # 10-19
  country.append((float(line_file[5])+float(line_file[6]))*1000) # 20-29
  country.append((float(line_file[7])+float(line_file[8]))*1000) # 30-39
  country.append((float(line_file[9])+float(line_file[10]))*1000) # 40-49
  country.append((float(line_file[11])+float(line_file[12]))*1000) # 50-59
  country.append((float(line_file[13])+float(line_file[14]))*1000) # 60-69
  country.append((float(line_file[15])+float(line_file[16]))*1000) # 70-79
  country.append((float(line_file[17])+float(line_file[18])+float(line_file[19])+float(line_file[20])+float(line_file[21]))*1000) # 80+
  
  
  #FV.append([line_file[0],((country[1]*cfr_base[1]+country[2]*cfr_base[2]+country[3]*cfr_base[3]+country[4]*cfr_base[4]+country[5]*cfr_base[5]+country[6]*cfr_base[6]+country[7]*cfr_base[7]+country[8]*cfr_base[8]+country[9]*cfr_base[9])/(pop_base[1]*cfr_base[1]+pop_base[2]*cfr_base[2]+pop_base[3]*cfr_base[3]+pop_base[4]*cfr_base[4]+pop_base[5]*cfr_base[5]+pop_base[6]*cfr_base[6]+pop_base[7]*cfr_base[7]+pop_base[8]*cfr_base[8]+pop_base[9]*cfr_base[9]))])
  FV_tmp1 = (country[1]*cfr_base[1])/pop_base[1]
  FV_tmp2 = (country[2]*cfr_base[2])/pop_base[2]
  FV_tmp3 = (country[3]*cfr_base[3])/pop_base[3]
  FV_tmp4 = (country[4]*cfr_base[4])/pop_base[4]
  FV_tmp5 = (country[5]*cfr_base[5])/pop_base[5]
  FV_tmp6 = (country[6]*cfr_base[6])/pop_base[6]
  FV_tmp7 = (country[7]*cfr_base[7])/pop_base[7]
  FV_tmp8 = (country[8]*cfr_base[8])/pop_base[8]
  FV_tmp9 = (country[9]*cfr_base[9])/pop_base[9]
  
  FV.append([line_file[0],(FV_tmp1 + FV_tmp2 + FV_tmp3 + FV_tmp4 + FV_tmp5 + FV_tmp6 + FV_tmp7 + FV_tmp8 + FV_tmp9)])
  
  #if(country[0] == 'United States of America'):
    #print(country)
	#print(FV_tmp1,FV_tmp2,FV_tmp3,FV_tmp4,FV_tmp5,FV_tmp6,FV_tmp7,FV_tmp8,FV_tmp9)
	#print(FV[-1])
  
#for fv_country in FV:
  #print("Country: ", fv_country[0], " FV: ", fv_country[1])
  
    #obitos = 314268
    #print(country[0], obitos/(FV*CFR_base))


output = []
offset = 0 #jump first line

for line_file in database2_deaths:
  if(offset == 0):
	offset = offset + 1
	continue
  
  line_file = line_file.replace('\n','')
  output.append(line_file)
  line_file = line_file.split(",")
  
  
  for contryFV in FV:
    if(contryFV[0] == line_file[0]):
	  if(line_file[4] == ''): line_file[4] = 0.0 #total_deaths
	  obitos = float(line_file[4])
	  
	  output[-1] = output[-1] + "," + str(int((obitos/(contryFV[1]*CFR_base))))
	  break

with open('output.csv', 'w') as f:
  f.write('location,date,new_cases,new_deaths,total_deaths,total_cases,total_cases_calculado\n')
  for line_file in output:
	f.write(line_file + '\n')











