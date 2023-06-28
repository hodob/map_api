import React, { useEffect, useState } from "react";
import KakaoMap from "./components/KakaoMap";
import useGeoLocation from "./components/useGeolocation";
import { Map, MapMarker, CustomOverlayMap } from 'react-kakao-maps-sdk';
import Axios from "axios";
import "./MainLayout.css"
type LatLngType = {
    lat: number;
    lng: number;
};

type MakerDataType = {
    title: string;
    latlng: {
        lat: number;
        lng: number;
    };
};



function MainLayout() {
    const location = useGeoLocation();
    const [maker, setMaker] = useState<MakerDataType[]>();
    const [isOpenMap, setIsOpenMap] = useState<{ id: string, data:boolean }[]>([]);

    const CreateApiCall = async () => {
        try {
            const response = await Axios.get('http://localhost:8000/map/test2');
            setMaker(response.data)
            console.log("통신시작")
            console.log(maker)
            console.log("통신끝")
        } catch (err) {
            console.log("Error >>", err);
        }
    }
    console.log(maker)
    if(!maker){ CreateApiCall()}
    useEffect(() => {
        
        if (maker) {
            const updatedIsOpenMap:{ id: string, data:boolean }[] = [];
            for (let i = 0; i < maker.length; i++) {
              updatedIsOpenMap.push({ id: maker[i].title, data: false });
            }
            console.log(updatedIsOpenMap)
            setIsOpenMap(updatedIsOpenMap);
        }
    }, []);


    // const [isOpen, setIsOpen] = useState(false)

    // const markerPosition = { lat: 35.2417951, lng: 129.0834828 }
    


    return (
        <>
            <div className="App">{location.loaded ? JSON.stringify(location) : "Location data not available yet."}</div>
            <Map
                center={{ lat: 35.2417951, lng: 129.0834828 }}
                style={{ width: "100%", height: "360px" }}
            >
                {maker?.map((item, index) => (
                    <React.Fragment key={`${item.title}-${index}`}>
                        {/* {isOpenMap.find(a => a.id === item.title)?.data && (
                            <CustomOverlayMap position={item.latlng}>
                                <div className="wrap">
                                    <div className="info">
                                        <div className="title">
                                            카카오 스페이스닷원
                                            <div
                                                className="close"
                                                // onClick={() => setIsOpenMap(false)} 
                                                //prevState.map((item) => (item.id === id ? { ...item, data: value } : item))
                                                onClick={() => setIsOpenMap(isOpenMap.map((a)=>(a.id===item.title ? {...a, data:false}:a)))}
                                                title="닫기"
                                            ></div>
                                        </div>
                                        <div className="body">
                                            내용
                                        </div>
                                    </div>
                                </div>
                                ;
                            </CustomOverlayMap>
                        )} */}
                        {/* <MapMarker position={item.latlng} onClick={() =>setIsOpenMap(isOpenMap.map((a)=>(a.id===item.title ? {...a, data:true}:a)))} /> */}
                        <MapMarker position={item.latlng} onClick={()=>{
                            console.log(item.title)
                            console.log(isOpenMap)
                            }} />
                    </React.Fragment>
                ))}

            </Map>



            {/* 
            <Map
                center={{ lat:35.2417951, lng: 129.0834828 }}
                style={{ width: "100%", height: "360px" }}
            >
                {maker?.map((item,index)=>(
                    <MapMarker
                    key={`${item.title}-${item.latlng}`}
                    position={item.latlng}
                    image={{
                        src: "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png", // 마커이미지의 주소입니다
                        size: {
                          width: 24,
                          height: 35
                        }, // 마커이미지의 크기입니다
                      }}
                      title={item.title}
                    ></MapMarker>
                ))}
            </Map>

             */}

        </>
    );
}

export default MainLayout;