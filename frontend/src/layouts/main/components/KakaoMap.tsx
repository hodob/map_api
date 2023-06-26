import React, { useEffect } from 'react';



declare global {
  interface Window {
    kakao: any;
  }
}
function KakaoMap (location:any) {
  if(location){
    console.log("1111")
  } else (
    console.log("2222")
  )

  useEffect(() => {
    if(location){
      console.log("1111")
    } else (
      console.log("2222")
    )
      window.kakao.maps.load(function() {
        const container :any= document.getElementById('map');
        const options :any= {
          center: new window.kakao.maps.LatLng(35.2397951, 129.0814828),
          // center: new window.kakao.maps.LatLng(location.location.lat, location.location.lng),
          level: 3
        };
        const map = new window.kakao.maps.Map(container, options);
        });

    return () => {
    };
  }, []);

  // return <div id="map" style={{ width: '5000px', height: '4000px' }}></div>;
  return <div id="map" style={{ width: '90vw', height: '80vh' }}></div>;
  
};

export default KakaoMap;