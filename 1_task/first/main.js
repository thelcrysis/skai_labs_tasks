import './style.css';
import {Map, View, Feature} from 'ol';
import {Polygon} from 'ol/geom';
import {Vector as VectorSource} from 'ol/source';
import {Vector as VectorLayer} from 'ol/layer';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import polygon from './polygon.json';


const coordinates = polygon["polygon"]
console.log(coordinates)
// getJSON(POLYGON_PATH, function(json) {
//   console.log(json); // this will show the info it in firebug console
// });

var feature = new Feature({
  geometry: new Polygon([coordinates])
});

feature.getGeometry().transform('EPSG:4326', 'EPSG:3857');
var vectorSource= new VectorSource({
        features: [feature ]
    });
console.log(vectorSource);
var vectorLayer = new VectorLayer({
      source: vectorSource
  });

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    }),
    vectorLayer
  ],
  view: new View({
    center: [0,0],
    zoom: 2
  })
});
// Centering and zooming in on the polygon
map.getView().fit(vectorSource.getExtent(), map.getSize())
// Zoom out a bit so there is some padding around the polygon
map.getView().setZoom(map.getView().getZoom() * 0.9);