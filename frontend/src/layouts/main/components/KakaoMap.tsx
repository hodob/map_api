import React, { useEffect } from 'react';
import useGeoLocation from "./useGeolocation";
import test from "../../../assets/images/test.jpg"
import "./KaKaoMap.css"
import Test from './test';

declare global {
  interface Window {
    kakao: any;
  }
}

function KakaoMap() {
  const location = useGeoLocation();
  useEffect(() => {
    window.kakao.maps.load(function () {
      const container: any = document.getElementById('map');
      const options: any = {
        // center: new window.kakao.maps.LatLng(35.2397951, 129.0814828),
        center: new window.kakao.maps.LatLng(location.coordinates?.lat, location.coordinates?.lng),
        level: 3
      };
      const map = new window.kakao.maps.Map(container, options);
      const imageSrc = '/img/test.jpg' // 마커이미지의 주소입니다  
      // const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png' // 마커이미지의 주소입니다  
      const imageSize = new window.kakao.maps.Size(64, 69) // 마커이미지의 크기입니다
      const  imageOption = { offset: new window.kakao.maps.Point(27, 69) }; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다


      // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
      const markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
        markerPosition = new window.kakao.maps.LatLng(location.coordinates?.lat, location.coordinates?.lng); // 마커가 표시될 위치입니다
      const marker = new window.kakao.maps.Marker({
        position: markerPosition,
        image: markerImage // 마커이미지 설정 
      });
      marker.setMap(map);  


      // 커스텀 오버레이에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
      const content = '<div class="wrap">' + 
      '    <div class="info">' + 
      '        <div class="title">' + 
      '            카카오 스페이스닷원' + 
      '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' + 
      '        </div>' + 
      '        <div class="body">' + 
      '            <div class="img">' +
      '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
      '           </div>' + 
      '            <div class="desc">' + 
      '                <div class="ellipsis">제주특별자치도 제주시 첨단로 242</div>' + 
      '                <div class="jibun ellipsis">(우) 63309 (지번) 영평동 2181</div>' + 
      '                <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>' + 
      '            </div>' + 
      '        </div>' + 
      '    </div>' +    
      '</div>';
      
      // document.querySelector("#map > div:nth-child(7) > div > div:nth-child(6) > div:nth-child(2) > div > div > div.title > div")
    // 마커를 중심으로 커스텀 오버레이를 표시하기위해 CSS를 이용해 위치를 설정했습니다
    var infoTitle = document.querySelectorAll('.info');

    // 코드에 적용한 '인포윈도우에 표출될 내용'을 담은 태그에 적용한 class명(혹은id명)을 선택자를 이용하여 불러온다.
    infoTitle.forEach(function(e: any) {
      e.parentElement.parentElement.onclick=closeOverlay
      // var w = e.offsetWidth + 10;
      // e.parentElement.style.width = w;  
      // e.parentElement.style.position = "relative";
      // if (e.className.includes('inactive')){
      //   e.parentElement.previousSibling.style.backgroundImage = "url('https://user-images.githubusercontent.com/81412212/174342201-0ec0c927-97f1-49dd-8c23-d6a872d9dfad.png')"; //꼭지
      // } else {
      //   e.parentElement.previousSibling.style.backgroundImage = "url('https://user-images.githubusercontent.com/81412212/174341207-bbaa6a46-2d67-4731-8a51-9a429488affa.png')"; //꼭지
      // }
      // e.parentElement.parentElement.style.display = "flex"; 
      // e.parentElement.parentElement.style.background = "none"; 
      // e.parentElement.parentElement.style.border = "none";
      // e.parentElement.parentElement.style.justifyContent = "center"; 
      // e.childNodes[1].style.display = "block";
      // e.childNodes[1].style.margin ="-8px";
      // e.parentElement.style.top = "-12px";
      // e.parentElement.style.top = "3px";
    })







var overlay = new window.kakao.maps.CustomOverlay({
  content: content,
  map: map,
  position: marker.getPosition()       
});
    window.kakao.maps.event.addListener(marker, 'click', function() {
      overlay.setMap(map);
  });
    function closeOverlay() {
      console.log("Test")
      // overlay.setMap(null);     
  }



      // ####################################

    });

    return () => {
    };
  }, [location]);

  return <div id="map" style={{ width: '90vw', height: '80vh' }}></div>;

};

export default KakaoMap;