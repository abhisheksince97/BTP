# BTP
B.Tech Project

1. Ground Truth and Results:
    It contains ground truth data for 5 districts of up. For each district, the major events during 2011-2018 period are listed. We have     also categorized each event on the basis of scale and type. In the third sheet (“Event Categories”) of each excel file, a column         named “Useful” is listed which shows whether we consider that event for accuracy and recall calculations or not.

    The script named “result_cal.ipynb”:
    
    Input: 
    1.  anomalies20.pk: output from Satellite event detection script in “\BTP\Satellite\Scripts\satellite_event_detection.ipynb”. It             contains around 20 anomaly dates detected as anomalies from satellite event detection.
    2.  anomalies25mm.pk: output from Satellite event detection script in “\BTP\Mass Media\Scripts\mass_media_anomaly_detection.ipynb”.         It contains around 25 anomaly dates detected as anomalies from satellite event detection.
    3.  Ground truth files (“agra_big.xlsx”, ..., “Varanasi_big.xlsx”)

    Output:
    
    “result.xlsx”: It contains analyses (graphs for precision and recall) for each district in a separate sheet. The last sheet named       “Average” contains the average precision and recall values over all 5 districts.

2. Satellite:
    It contains “earthengine_script.js”. If we run this this script on google earth engine than it outputs “Avg_NL_Dist_cf_cvg.csv”.
    It also contains “satellite_event_detection.ipynb” which runs several event detection algorithms on data to output anomalous dates       which may represent an event.
    
    Input: 
        “/Satellite/Data/Avg_NL_Dist_cf_cvg.csv”: Contains Average nightlight values for each district on monthly basis ( April 2012 –            April 2018).
        
    Output: 
    
        “anomalies20.pk”

3. Mass Media:
    It contains “/Scripts/mapping.ipynb”.
    
    Input: 
    
    1. “/Data/city_map_big.pk”
    2. “/Data/state_map_big.pk”
    3. “/Data/Districts/up.txt”
    4. “/Data/SmartStoplist.txt” 
    
    Output:
    
    “/Data/up/mediaDataVectors_”+City_name+”_big.pk”: 5 files for 5 cities. 
    It contains “/Scripts/mass_media_anomaly_detection.ipynb”.
    
    Input: 
    
    “/Data/up/mediaDataVectors_”+City_name+”_big.pk”
    
    Output: 
    
    “anomalies25mm.pk”

