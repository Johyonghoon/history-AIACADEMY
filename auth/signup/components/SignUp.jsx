import { signupApi } from 'auth/signup/api'
import 'auth/signup/styles/SignUp.css'
import { useState } from 'react'

const SignUp = () => {
    const [inputs, setInputs] = useState({})
    const {email, nickname, password} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const signuprequest = {email, nickname, password}
        alert(`사용자 이름: ${JSON.stringify(signuprequest)}`)
        signupApi(signuprequest)
    }

    return (<>
    <h1>계정 생성</h1>
    <p>계정 생성을 위해 다음 양식을 입력해주세요.</p>

    <b>Email</b>
    <input type="text" placeholder="이메일" name="email" onChange={onChange}/><br/>

    <b>nickname</b>
    <input type="text" placeholder="닉네임" name="nickname" onChange={onChange}/><br/>

    <b>Password</b>
    <input type="password" placeholder="비밀번호" name="password" onChange={onChange}/><br/><br/>
    
    <button type="button">취소</button>
    <button onClick={onClick}>회원가입</button>
    </>)
}

export default SignUp