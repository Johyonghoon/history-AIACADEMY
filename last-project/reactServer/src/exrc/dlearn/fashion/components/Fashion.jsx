import { useState } from "react"
import dlearnService, { apiFashionGetMethodByAxios } from "../api"

const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {test_num} = inputs

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onGetClickByAxios = e => {
        e.preventDefault()
        alert(`사용자 이름: ${JSON.stringify(test_num)}`)
        apiFashionGetMethodByAxios(test_num)
        .then((res)=>{
            alert(`옷의 카테고리 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('숫자를 다시 입력해주세요.')
        })
    }
    const onGetClickByPromise = e => {
        e.preventDefault()
        dlearnService.apiFashionGetMethodByPromise(test_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    const onPostClickByPromise = e => {
        e.preventDefault()
        dlearnService.apiFashionPostMethodByPromise(test_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(<>
    <h1>FASHION</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" className="box" placeholder="테스트할 옷 번호" name="test_num" onChange={onChange}/>
    
    <form method="get">
    <button onClick={onGetClickByAxios}>옷의 카테고리 찾기(Get/axios)</button>
    <button onClick={onGetClickByPromise}>옷의 카테고리 찾기(Get/promise)</button>
    </form>
    <form method="post">
    <button onClick={onPostClickByPromise}>옷의 카테고리 찾기(Post/promise)</button>
    </form>
    </>)
}

export default Fashion