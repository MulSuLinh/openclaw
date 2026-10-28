const products=[
{id:1,name:"Robusta rang mộc",desc:"Đậm đà, hậu vị mạnh, hợp pha phin truyền thống.",price:120000,image:"https://images.unsplash.com/photo-1559525839-b184a4d698c7?auto=format&fit=crop&w=800&q=80"},
{id:2,name:"Arabica thơm nhẹ",desc:"Hương thơm thanh, vị chua dịu và cân bằng.",price:165000,image:"https://images.unsplash.com/photo-1559525839-8f275b3c5edd?auto=format&fit=crop&w=800&q=80"},
{id:3,name:"Cà phê phối trộn",desc:"Phối vị hài hòa, phù hợp uống mỗi ngày.",price:140000,image:"https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?auto=format&fit=crop&w=800&q=80"}
];
const cart={};
const money=n=>new Intl.NumberFormat("vi-VN").format(n)+"đ";
const productRoot=document.getElementById("products");
productRoot.innerHTML=products.map(p=>'<article class="product"><img src="'+p.image+'" alt="'+p.name+'" loading="lazy"><div class="product-body"><h3>'+p.name+'</h3><p>'+p.desc+'</p><div class="price-row"><span class="price">'+money(p.price)+'</span><button class="add" type="button" data-add="'+p.id+'">+ Thêm</button></div></div></article>').join("");
function renderCart(){
 const items=products.filter(p=>cart[p.id]);
 document.getElementById("cart-count").textContent=items.reduce((n,p)=>n+cart[p.id],0);
 document.getElementById("cart-items").innerHTML=items.length?items.map(p=>'<div class="cart-line"><span>'+p.name+' × '+cart[p.id]+'</span><span>'+money(p.price*cart[p.id])+' <button type="button" data-remove="'+p.id+'" aria-label="Bỏ một sản phẩm">−</button></span></div>').join(""):"Giỏ hàng đang trống. Hãy chọn sản phẩm bên trên nhé!";
 document.getElementById("cart-total").textContent=money(items.reduce((n,p)=>n+p.price*cart[p.id],0));
}
document.addEventListener("click",e=>{const add=e.target.closest("[data-add]");const remove=e.target.closest("[data-remove]");if(add){const id=Number(add.dataset.add);cart[id]=(cart[id]||0)+1;renderCart()}if(remove){const id=Number(remove.dataset.remove);cart[id]--;if(cart[id]<=0)delete cart[id];renderCart()}});
document.getElementById("order-form").addEventListener("submit",e=>{
 e.preventDefault();const items=products.filter(p=>cart[p.id]);if(!items.length){document.getElementById("order-result").textContent="Bạn hãy thêm ít nhất một sản phẩm vào giỏ hàng.";return}
 const lines=items.map(p=>'- '+p.name+' x '+cart[p.id]+': '+money(p.price*cart[p.id])).join('\n');
 const total=items.reduce((n,p)=>n+p.price*cart[p.id],0);
 const order='ĐƠN ĐẶT HÀNG — MỘC COFFEE\nTên: '+document.getElementById("customer-name").value+'\nSĐT: '+document.getElementById("customer-phone").value+'\nĐịa chỉ: '+document.getElementById("customer-address").value+'\nSản phẩm:\n'+lines+'\nTổng: '+money(total)+'\nGhi chú: '+(document.getElementById("customer-note").value||'Không có');
 const box=document.getElementById("order-result");box.innerHTML='<p><strong>Đã tạo nội dung đơn hàng demo.</strong></p><textarea id="order-copy" readonly style="width:100%;min-height:190px;padding:12px;border:1px solid #ddcfbd;border-radius:10px"></textarea><button class="add" type="button" id="copy-order">Sao chép đơn hàng</button>';document.getElementById("order-copy").value=order;document.getElementById("copy-order").addEventListener("click",async()=>{try{await navigator.clipboard.writeText(order);document.getElementById("copy-order").textContent="Đã sao chép!"}catch{document.getElementById("order-copy").select();document.execCommand("copy");document.getElementById("copy-order").textContent="Hãy sao chép nội dung đã chọn"}})
});
document.getElementById("year").textContent=new Date().getFullYear();renderCart();
