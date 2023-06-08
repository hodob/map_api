import React from "react";
import KakaoMap from "./components/KakaoMap";

function MainLayout() {
    console.log(process.env.REACT_APP_KAKAO_MAP_API_KEY)
    return (
        <>
        
        <h1>hello worlfd</h1>
        <KakaoMap/>
        </>
    );
}

export default MainLayout;