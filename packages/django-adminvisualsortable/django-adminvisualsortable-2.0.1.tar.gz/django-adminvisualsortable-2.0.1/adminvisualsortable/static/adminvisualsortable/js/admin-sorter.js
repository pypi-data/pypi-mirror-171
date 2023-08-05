(function() {
    let title_height = 0;
    let elements = document.querySelectorAll('.item-title');
    for ( let i=0; i<elements.length; i++) {
        let get_height = elements[i].offsetHeight;
        if ( get_height > title_height )
            title_height = get_height;
    }
    for ( let i=0; i<elements.length; i++) {
        elements[i].style.height = title_height + 'px';
    }
    let sorting_cont = document.getElementById('sortable-items-cont');
    let sortable = Sortable.create(sorting_cont, {
        animation: 150,
        ghostClass: 'drop-target',
        chosenClass: "drop-active",
        onEnd: function (evt) {
            let elements = document.getElementsByClassName("dropzone");
            let elementsArray = new Array();
            let idxArray = [];
            for (let i = 0; i < elements.length; i++) {
                let el = elements[i];
                elementsArray.push({
                    'id': parseInt(el.dataset.id),
                    'idx': parseInt(el.dataset.ord),
                });
                idxArray.push(parseInt(el.dataset.ord));
            }
            idxArray.sort((a, b) => a - b);
            for (let i = 0; i < elementsArray.length; i++) {
                elementsArray[i].idx = idxArray[i];
            }
            body = {
                dict_id_idx: elementsArray,
                model_name: djvars.model_name,
                app: djvars.app,
                model_parent: djvars.model_parent,
            };
            fetch(djvars.urls.api_sort_model, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': djvars.csrf_token,
                },
                body: JSON.stringify(body)
            })
            .then(resp => resp.json())
            .then(responseData => {
                if (responseData.status == 'success' ) {
                    for (let i = 0; i < elementsArray.length; i++) {
                        document.querySelector(`.live-ord[data-id="${elementsArray[i].id}"]`).innerHTML = elementsArray[i].idx;
                    }
                } else {
                    console.warn(responseData.message);
                    alert('An Error occurred while saving models');
                }
            })
            .catch(error => {
                alert('An issue with the server has been detected:\n'+error);
            })
        }
    });
})();
