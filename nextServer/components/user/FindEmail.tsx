export default function FindEmail() {
    return (
    <>    
        <h1>이메일 찾기</h1>
        <form action="/send-data-here">
            <label htmlFor="user_name">성함 : </label>
            <input type="text" id="user_name" name="user_name" required/>
            <label htmlFor="phone">전화번호 :</label>
            <input type="text" id="phone" name="phone" required/>
            <button type="submit">Submit</button>
        </form>
    </>
    );
}
