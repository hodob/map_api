import React from "react";
import KakaoMap from "./components/KakaoMap";
import useGeoLocation from "./components/useGeolocation";
import { Map,MapMarker } from 'react-kakao-maps-sdk';

function MainLayout() {
    const location = useGeoLocation();
    
    return (
        <>
            <div className="App">
                {location.loaded ? JSON.stringify(location)
      : "Location data not available yet."}
            </div>
        {/* <KakaoMap/> */}
        <Map
      center={{ lat: 33.5563, lng: 126.79581 }}
      style={{ width: "100%", height: "360px" }}
    >
      <MapMarker position={{ lat: 33.55635, lng: 126.795841 }}>
        <div style={{color:"#000"}}>Hello World!</div>
      </MapMarker>
    </Map>

        </>
    );
}

export default MainLayout;