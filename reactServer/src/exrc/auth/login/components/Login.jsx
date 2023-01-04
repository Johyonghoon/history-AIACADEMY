import 'exrc/auth/login/styles/Login.css'
import { useState } from 'react'
import { apiLogin } from '../api'
import { useNavigate } from 'react-router-dom'

const Login = () => {
    const [inputs, setInputs] = useState({})
    const {user_email, password} = inputs
    const history = useNavigate()

    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
      e.preventDefault()
      const request = {user_email, password}
      alert(`사용자 이름: ${JSON.stringify(request)}`)
      apiLogin(request)
      .then((res)=>{
          localStorage.getItem("loginUser", JSON.stringify(request))
          alert(`response is ${JSON.stringify(res.data)}`)
          history("/home")
      })
      .catch((err) => {
          console.log(err)
          alert('이메일과 비밀번호를 다시 입력해주세요.')
      })
    }
    return (<>
    
    <h1>로그인</h1>
    <p>로그인을 위해 아이디와 비밀번호를 입력해주세요.</p>

    <b>아이디/비밀번호</b>
    <input type="text" placeholder="이메일 입력" name="user_email" onChange={onChange}/>

    <b>비밀번호</b>
    <input type="password" placeholder="비밀번호 입력" name="password" onChange={onChange}/>
        
    <button onClick={onClick}>로그인</button>
    </>)
}

export default Login