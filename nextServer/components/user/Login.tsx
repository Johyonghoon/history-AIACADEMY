export default function Login() {
    return (<>
    
    <h1>로그인</h1>
    <form action="/send-data-here" method="post">
        <label htmlFor="first">First name:</label>
        <input type="text" id="user_email" name="user_email" required/>
        <label htmlFor="last">Last name:</label>
        <input type="text" id="password" name="password" required/>
        <button type="submit">Submit</button>
    </form>
    </>)
}
