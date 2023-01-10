export default function ListForm({list: []}){
    return <><h2>유저 목록</h2>
    <table className='user-list'>
        <thead>
            <tr>
            <th>user_id</th>
            <th>user_email</th>
            <th>password</th>
            <th>user_name</th>
            <th>phone</th>
            <th>birth</th>
            <th>address</th>
            <th>job</th>
            <th>user_interests</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    </>
}