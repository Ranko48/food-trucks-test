import React, { useState } from "react";

import { MarkerF, InfoWindowF } from "@react-google-maps/api";


const Marker = ({
  selectedMarker,
  index,
  openInfoWindow,
  closeInfoWindow,
  marker
}) => {

  return (
    <MarkerF
      key={index}
      onClick={() =>{ openInfoWindow(marker); console.log(marker)}}
      position={{lat: marker.lat, lng: marker.lng}}
    >
      {selectedMarker?.id === marker?.id && (
        <InfoWindowF position={{lat: marker.lat, lng: marker.lng}} onCloseClick={closeInfoWindow}>
          <div className="bg-white p-2 rounded shadow">
            <h3 className="font-bold text-lg">{marker.name}</h3>
            <p className="text-sm"><span className="font-bold">Address:</span> {marker.address}</p>
            <p className="text-sm"><span className="font-bold">Facility_Type:</span> {marker.facility_type}</p>
            <p className="text-sm"><span className="font-bold">Distance:</span> {marker.distance}</p>
          </div>
        </InfoWindowF>
      )}
    </MarkerF>
  );
}

export default Marker
