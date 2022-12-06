import 'auth/styles/SignUp.css'

const SignUp = () => {
    return (<>
    <h1>계정 생성</h1>
    <p>계정 생성을 위해 다음 양식을 입력해주세요.</p>

    <label for="email"><b>Email</b></label><br/>
    <input type="text" placeholder="이메일 입력" name="email" required/><br/><br/>

    <label for="psw"><b>Password</b></label><br/>
    <input type="password" placeholder="비밀번호 입력" name="psw" required/><br/><br/>

    <label for="psw-repeat"><b>Repeat Password</b></label><br/>
    <input type="password" placeholder="비밀번호 확인" name="psw-repeat" required/><br/><br/>
    
    <button type="button">취소</button>
    <button type="submit">회원가입</button>
    </>)
}

export default SignUp