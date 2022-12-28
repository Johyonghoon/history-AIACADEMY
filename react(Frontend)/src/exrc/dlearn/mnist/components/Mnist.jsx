import { useState } from "react"
import dlearnService from "../api"

const Mnist = () => {
    const [inputs, setInputs] = useState({})
    const {test_num} = inputs

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClickGetMethod = e => {
        e.preventDefault()
        dlearnService.apiMnistGetMethod(test_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    const onClickPostMethod = e => {
        e.preventDefault()
        dlearnService.apiMnistPostMethod(test_num)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(<>
    <h1>FASHION</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" className="box" placeholder="테스트 번호(찾고자 하는 숫자가 아님)" name="test_num" onChange={onChange}/>
    
    <form method="get">
    <button onClick={onClickGetMethod}>숫자 찾기(Get)</button>
    </form>
    <form method="post">
    <button onClick={onClickPostMethod}>숫자 찾기(Post)</button>
    </form>
    </>)
}

export default Mnist