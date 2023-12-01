import React, { useState, useEffect } from "react";
import { GoogleMap, LoadScript, MarkerF } from "@react-google-maps/api";
import axios from "axios";

import CustomInput from "./components/CustomInput";
import CustomMarker from "./components/CustomMarker";
const GOOGLE_API_KEY = "AIzaSyDP_1Mzt-AqRmyxWZgcuZ1mak9AFRyvoeQ";

const App = () => {
  const [center, setCenter] = useState(); // Store the center coordinates of the map
  const [lat, setLat] = useState(""); // Store the latitude value
  const [lng, setLng] = useState(""); // Store the longitude value
  const [markers, setMarkers] = useState([]); // Store the array of food truck markers
  const [selectedMarker, setSelectedMarker] = useState(null); // Store the currently selected marker
  const [zoom, setZoom] = useState(4); // Store the zoom level of the map

  useEffect(() => {
    // Get the current location of the user
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setLat(parseFloat(latitude));
          setLng(parseFloat(longitude));
          if (latitude && longitude && !isNaN(latitude) && !isNaN(longitude)) {
            setCenter({ lat: parseFloat(latitude), lng: parseFloat(longitude) });
          }
        },
        (error) => {
          console.error("Error getting current location:", error);
        }
      );
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  }, []);

  const containerStyle = {
    width: "800px",
    height: "500px",
  };

  const handleLatChange = (e) => {
    // Update the latitude value when the input changes
    const value = e.target.value;
    value === "" ? setLat(parseFloat(0)) : setLat(parseFloat(value));
  };

  const handleLngChange = (e) => {
    // Update the longitude value when the input changes
    const value = e.target.value;
    value === "" ? setLng(parseFloat(0)) : setLng(parseFloat(value));
  };

  const handleMarkerDrag = (event) => {
    // Update the latitude and longitude values when the marker is dragged
    const { latLng } = event;
    setLat(latLng.lat());
    setLng(latLng.lng());
  };

  const openInfoWindow = (marker) => {
    // Set the selected marker when its info window is opened
    setSelectedMarker(marker);
  };

  const closeInfoWindow = () => {
    // Clear the selected marker when the info window is closed
    setSelectedMarker(null);
  };

  const handleSearch = () => {
    // Fetch nearby food trucks based on the provided latitude and longitude values
    const url = `http://localhost:8000/api/nearby-food-trucks/?latitude=${lat}&longitude=${lng}`;

    axios
      .get(url)
      .then((response) => {
        const res = response.data.food_trucks;
        setMarkers(res);
        setCenter({ lat: parseFloat(res[0].lat), lng: parseFloat(res[0].lng) });
        setZoom(12);
      })
      .catch((error) => {
        console.error("Error fetching nearby food trucks:", error);
      });
  };

  return (
    <>
      <div className="relative px-6 lg:px-8">
        <div className="mx-auto max-w-2xl py-8 sm:py-8 lg:py-8">
          <div className="hidden sm:mb-6 sm:flex sm:justify-center">
            <div className="text-center">
              <h2 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-3xl py-5">
                Food Trucks Finder
              </h2>
              <div className="flex flex-col mb-4 sm:flex-row sm:items-center">
                <div className="flex-grow sm:mr-4">
                  <CustomInput
                    label="Latitude:"
                    value={String(lat)}
                    onChange={handleLatChange}
                  />
                </div>
                <div className="flex-grow sm:mr-4">
                  <CustomInput
                    label="Longitude:"
                    value={lng}
                    onChange={handleLngChange}
                  />
                </div>
                <button
                  type="submit"
                  className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  onClick={handleSearch}
                >
                  Search
                </button>
              </div>
              <LoadScript googleMapsApiKey={GOOGLE_API_KEY}>
                <GoogleMap
                  mapContainerStyle={containerStyle}
                  center={center}
                  zoom={zoom}
                >
                  {center && (
                    <MarkerF
                      position={{
                        lat: lat,
                        lng: lng,
                      }}
                      draggable
                      onDrag={handleMarkerDrag}
                      icon={"http://maps.google.com/mapfiles/ms/icons/green-dot.png"}
                    />
                  )}

                  {markers.map((marker, index) => (
                    <CustomMarker
                      key={index}
                      openInfoWindow={openInfoWindow}
                      closeInfoWindow={closeInfoWindow}
                      selectedMarker={selectedMarker}
                      marker={marker}
                    >
                      {/* Additional custom marker components */}
                    </CustomMarker>
                  ))}
                </GoogleMap>
              </LoadScript>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default App;
