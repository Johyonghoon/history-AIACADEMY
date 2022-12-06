import 'auth/styles/Login.css'

const Login = () => {
    return (<>
    
    <h1>로그인</h1>
    <p>로그인을 위해 아이디와 비밀번호를 입력해주세요.</p>

    <label for="uname"><b>아이디</b></label><br/>
    <input type="text" placeholder="아이디 입력" name="uname" required/><br/><br/>

    <label for="psw"><b>비밀번호</b></label><br/>
      <input type="password" placeholder="비밀번호 입력" name="psw" required/><br/><br/>
        
    <button type="submit">로그인</button>
    <button type="button">취소</button><br/>
    <span><h5><a href="#">비밀번호</a>를 잊으셨나요?</h5></span><br/>
    </>)
}

export default Login