document.getElementById('submitButton').addEventListener('click', function () {
    const userName = document.getElementById('userName').value.trim();

    if (userName !== "") {
        // ユーザー名を次のページに渡す
        localStorage.setItem("userName", userName);
        window.location.href = "../home/home.html"; // 次のページへ移動
    } else {
        alert("名前を入力してください！");
    }
});