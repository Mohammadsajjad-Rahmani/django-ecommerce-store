function SendArticleComment(articleId) {
    // console.log('adsasasd')
    let comment = $('#ArticleCommentTextArea').val();
    let parentId = $('#parentId').val();
    // console.log(comment);
    $.get('/articels/add-article-comment', {
        articleComment: comment, articleId: articleId, parentId: parentId
    }).then(result => {
        // console.log(result)
        $('#comment_area').html(result);
        // html bargasht dade shode jaygozine code html ba id comment_are mishe result hamon html bargasht dade shode
        $('#ArticleCommentTextArea').val('');
        $('#parentId').val('');
        // console.log(result);
        if (parentId !== '' && parentId !== null) {
            document.getElementById('parentId' + parentId).scrollIntoView({behavior: 'smooth'});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior: 'smooth'});
        }
        // document.getElementById('comment_area').scrollIntoView({behavior: 'smooth'});
    });
//     $.get('/articels/add-article-comment', {
//         articleComment: comment,
//         articleId: articleId,
//         parentId: parentId
//     })
//     // vaqti az $ estefade mokonim darvae az ketab khone jquery estefade mikonim
//     //$.get('/articels/add-article-comment') ye darkhaste get mizane be on address va function mored nazar
//     location.reload()
// }
}

function SendProductComment(productId) {
    let comment = $('#ProductCommentTextArea').val();
    if (comment === '' || comment === null) {
        Swal.fire({
            title: 'اعلان',
            text: 'نظر شما باید حاوی متن و کاراکتر معتبر باشد ',
            icon: 'error',
            confirmButtonText: 'متوجه شدم',
            showCancelButton: false
        })
        return
    }
    $.get('/products/add-product-comment', {
        productComment: comment, productId: productId,
    }).then(result => {
        // $('#comments_area').html(result);
        console.log(result);
        if (result.status === 'success') {
            Swal.fire({
                title: 'اعلان',
                text: 'پیام شما با موفقیت ارسال شد پس از تایید ادمین پیام شما نمایش داده میشود ',
                icon: 'success',
                confirmButtonText: 'متوجه شدم',
                showCancelButton: false
            })
        }
        $('#ProductCommentTextArea').val('');

    })
}


function FillParentId(parentId) {
    $('#parentId').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: 'smooth'});
}

function filter_button() {

    // debugger
    const FilterValues = $('#sl2').val();
    const StartPrice = FilterValues.split(',')[0];
    const EndPrice = FilterValues.split(',')[1];
    $('#start_price').val(StartPrice);
    $('#end_price').val(EndPrice);

    $('#filter_form').submit();


}


function paginatorfunctipn(page) {

    $('#paginator').val(page);
    $('#filter_form').submit();
}


function ChangeAddress(ImageAddress) {
    $('#main_image').attr('src', ImageAddress);
    $('#show_large_image').attr('href', ImageAddress);

}

function ProductOrder(ProductId) {
    const ProductCount = $('#ProductCount').val();
    $.get('/order/add-to-product-order?product_id=' + ProductId + '&count=' + ProductCount).then(result => {
        console.log(result);
        // if (result.status === 'success') {
        //     Swal.fire({
        //         title: "اعلان",
        //         text: "محصول با موفقیت به سبد خرید افزووده شد",
        //         icon: "success"
        //     });
        // }
        // age be ravesh bala code benivisim koli code bayad benivisim
        Swal.fire({
            title: 'اعلان',
            text: result.text,
            icon: result.icon,
            confirmButtonText: result.confirmButtonText,
            showCancelButton: false
        }).then(confirm => {
            if (result.status === 'not-authenticated' && confirm.isConfirmed) {
                window.location.href = '/login'
            }
        });
    });
}


// double shift quick access to files
// ctrl + F5 remove js cache
// behtare bad az dastor haye ajaxi ctrl + f5 ro bezani ta js haye jadid load beshan


// function OnLineClass() {
//     let ClassName = document.getElementById('on-line-text')
//     ClassName.style.overflow = 'unset';
// }


function RemoveOrder(detailId){
    $.get('/user/remove-order-detail?detailId=' + detailId).then(result =>{
        // console.log(result);
        if (result.status === 'success'){
            $('#order-detail-content').html(result.html);
        }
    });
}



function ChangeOrderCount(detailId,state){
    $.get('/user/change-order-detail?detailId=' + detailId + '&state=' + state).then(result =>{
        if (result.status === 'success'){
            $('#order-detail-content').html(result.html);
        }
    });
}