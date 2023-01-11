export default function FindPassword() {
    return (
    <>    
        <h1>비밀번호 찾기</h1>
            <form action="/send-data-here">
                <label htmlFor="user_email">이메일 :</label>
                <input type="text"  id="user_email" name="user_email" required minLength= {10} maxLength={20}/>
                <button type="submit">Submit</button>
            </form> 
    </>
    );
}