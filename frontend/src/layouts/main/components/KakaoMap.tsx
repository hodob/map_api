import React, { useEffect } from 'react';
import useGeoLocation from "./useGeolocation";


declare global {
  interface Window {
    kakao: any;
  }
}



function KakaoMap ( ) {
  const location = useGeoLocation();
  useEffect(() => {
      window.kakao.maps.load(function() {
        const container :any= document.getElementById('map');
        const options :any= {
          // center: new window.kakao.maps.LatLng(35.2397951, 129.0814828),
          center: new window.kakao.maps.LatLng(location.coordinates?.lat, location.coordinates?.lng),
          level: 3
        };
        console.log("카카오지도2")
        const map = new window.kakao.maps.Map(container, options);
        });

    return () => {
    };
  }, [location]);

  // return <div id="map" style={{ width: '5000px', height: '4000px' }}></div>;
  return <div id="map" style={{ width: '90vw', height: '80vh' }}></div>;
  
};

export default KakaoMap;