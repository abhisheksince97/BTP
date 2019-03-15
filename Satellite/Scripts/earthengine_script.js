var viir = ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG");

var districts_fc=ee.FeatureCollection('ft:1CIw2JJ07M1xw9nQRAFo-K58txKQMN4tHva9IXvdX','geometry');
Map.addLayer(districts_fc)

var af = ee.FeatureCollection([]);

var out_mean = [];
var ind = 0;
var myarr = [];

var myfun = function(a){
  print(ind);
  print(myarr.length-1);
  var feat = a['features'];
  var ii = 0;
  for(var i in feat){
    if(ind === 0) out_mean[ii] = {};
    out_mean[ii]['District'] = feat[i]['properties'][ "Districtname"];
    // out_mean[ii][myarr[ind]['date']] = feat[i]['properties']['avg_rad'];
    out_mean[ii][myarr[ind]['date']] = feat[i]['properties']['cf_cvg'];
    ii += 1;
  }
  
  if(ind === myarr.length-1){
    print("complete");
    var new_arr = [];
    for( var u in out_mean){
      new_arr.push(ee.Feature(null, out_mean[u]));
    }
    af = ee.FeatureCollection(new_arr);
    print("done");
    print(af);
    Export.table.toDrive({
      collection:af,
      description:'Avg_NL_Dist',
      fileFormat: 'CSV'
    });
  }
  else{
    ind += 1;
    myarr[ind]['value'].evaluate(myfun);
  }
  return a;
}

for(var i=2;i<9;i++){
  for(var j=1;j<13;j++){
    var mm = j.toString();
    if(j < 10) mm = '0'+mm;
    if((i==2 && j<4) || (i==8 && j>4)) continue;
    var temp = '201' + i.toString() + '-' + mm.toString() + '-01';
    
    var viir_month_avg = viir.filterDate(temp).mean();
    var temp_coll = viir_month_avg.reduceRegions({
      collection: districts_fc,
      reducer: ee.Reducer.mean(),
      scale: 500
    });
    
    myarr[myarr.length] = {'date': temp, 'value': temp_coll};
  }
}

print("start");
myarr[0]['value'].evaluate(myfun);
