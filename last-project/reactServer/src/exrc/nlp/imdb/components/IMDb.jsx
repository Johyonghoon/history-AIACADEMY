import { useState } from "react"
import imdbService from "../api"

const IMDb = () => {
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClickPostMethod = e => {
        e.preventDefault()
        imdbService.apiPostMethod(inputs)
        .then(res => {
            const json = JSON.parse(res)
            setPositive(json["result"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(<>
    <h1>IMDb</h1>
    <p>긍정률을 확인하고 싶은 영화의 리뷰를 입력해주세요.</p>
    <input type="text" className="box" placeholder="리뷰 내용" name="inputs" onChange={onChange}/>
    <form method="post">
    <button onClick={onClickPostMethod}>긍정률 확인하기</button>
    </form>
    {positive}
    </>)
}

export default IMDb