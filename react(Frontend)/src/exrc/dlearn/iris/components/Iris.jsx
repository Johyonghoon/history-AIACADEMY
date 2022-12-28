import { apiIris } from "exrc/dlearn/iris/api/index"
import { useState } from "react"

const Iris = () => {
    const [inputs, setInputs] = useState({})
    const {sepal_width, sepal_length, petal_width, petal_length} = inputs

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const request = {sepal_width, sepal_length, petal_width, petal_length}
        alert(`사용자 이름: ${JSON.stringify(request)}`)
        apiIris(request)
        .then((res)=>{
            console.log(`Response is ${res.data.result}`)
            localStorage.setItem('token', JSON.stringify(res.data.result))
            alert(`찾는 품종 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('꽃잎,받침 길이/너비를 다시 입력해주세요')
        })
    }
    return(<>
    <h1>IRIS</h1>
    <p>붓꽃의 품종을 찾기위한 꽃의 정보를 입력해주세요.</p>
    <input type="text" placeholder="꽃받침의 너비 입력(cm)" name="sepal_width" onChange={onChange}/>
    <input type="text" placeholder="꽃받침의 길이 입력(cm)" name="sepal_length" onChange={onChange}/>
    <input type="text" placeholder="꽃잎의 너비 입력(cm)" name="petal_width" onChange={onChange}/>
    <input type="text" placeholder="꽃잎의 길이 입력(cm)" name="petal_length" onChange={onChange}/>

    <button onClick={onClick}>아이리스 품종 찾기</button>
    </>)
}

export default Iris