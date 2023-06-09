import React, { useEffect } from 'react';
declare global {
  interface Window {
    kakao: any;
  }
}
const KakaoMap = () => {
  
  useEffect(() => {
      const container :any= document.getElementById('map');
      const options :any= {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
      };
      new window.kakao.maps.Map(container, options);
    // };

    return () => {
      // Clean up the script when the component is unmounted
      // document.head.removeChild(script);
    };
  }, []);

  // return <div id="map" style={{ width: '5000px', height: '4000px' }}></div>;
  return <div id="map" style={{ width: '90vw', height: '80vh' }}></div>;
  
};

export default KakaoMap;