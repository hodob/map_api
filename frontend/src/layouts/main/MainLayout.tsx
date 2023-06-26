import React from "react";
import KakaoMap from "./components/KakaoMap";
import useGeoLocation from "./components/useGeolocation";

function MainLayout() {
    const location = useGeoLocation();
    
    return (
        <>
            <div className="App">
                {location.loaded ? JSON.stringify(location)
      : "Location data not available yet."}
            </div>
        <KakaoMap/>
        </>
    );
}

export default MainLayout;