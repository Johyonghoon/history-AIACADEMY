import dummyService from "../api"

export default function  DummyForm(){
    const onClick = e => {
        e.preventDefault()
        dummyService.apiDummyPostMethodByPromise()
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h2>더미 사용자 등록</h2>
    <button onClick={onClick}>더미 사용자 등록</button>
    <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
    </>)
}
