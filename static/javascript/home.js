document.getElementById('submitButton').addEventListener('click', function () {
    const inputField = document.getElementById('inputField');
    const displayArea = document.getElementById('displayArea');

    if (inputField.value.trim() !== "") {
        // 新しい要素を作成
        const newItem = document.createElement('div');
        newItem.textContent = inputField.value;

        // 削除ボタンを作成
        const deleteBtn = document.createElement('span');
        deleteBtn.textContent = " ✖️";
        deleteBtn.classList.add('delete-btn');

        // 削除ボタンの機能
        deleteBtn.addEventListener('click', function () {
            newItem.remove();
        });

        newItem.appendChild(deleteBtn);
        displayArea.appendChild(newItem);

        // 入力欄をクリア
        inputField.value = "";

        //調理ボタン
        const cooking = document.createElement('ga');
        cooking.textContent = inputField.value;

        // 調理ボタンの機能
        cooking.addEventListener('click', function () {
            
        });

        // 食材の数によって鍋の画像を切り替える関数
        function updateNabeImage() {
            const displayArea = document.getElementById('displayArea');
            const nabeImage = document.getElementById('nabeImage');

            if (displayArea.children.length > 0) {
                nabeImage.src = "../image/babehatena.png"; // 食材がある場合
            } else {
                nabeImage.src = "../image/nabe.png"; // 食材がない場合
            }
        }

        // 画像を更新
        updateNabeImage();


    }
});

document.getElementById('nextPageButton').addEventListener('click', function () {
    window.location.href = "../last/next.html"; // 移動先のページ
});
