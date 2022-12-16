import { useState } from "react"
import { fashion } from "../api"

const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {test_num} = inputs

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const request = {test_num}
        alert(`사용자 이름: ${JSON.stringify(request)}`)
        fashion(request)
        .then((res)=>{
            console.log(`Response is ${res.data.result}`)
            localStorage.setItem('token', JSON.stringify(res.data.result))
            alert(`옷의 카테고리 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('숫자를 다시 입력해주세요.')
        })
    }
    return(<>
    <h1>FASHION</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" placeholder="테스트할 옷 번호" name="test_num" onChange={onChange}/>

    <button onClick={onClick}>옷의 카테고리 찾기</button>
    </>)
}

export default Fashion