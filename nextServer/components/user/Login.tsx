export default function Login() {
    return (<>
    
    <h1>로그인</h1>
    <p>로그인을 위해 아이디와 비밀번호를 입력해주세요.</p>

    <b>아이디/비밀번호</b>
    <input type="text" placeholder="이메일 입력" name="user_email"/>

    <b>비밀번호</b>
    <input type="password" placeholder="비밀번호 입력" name="password"/>
        
    <button>로그인</button>
    </>)
}
