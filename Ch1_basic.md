# 筆記

本來的設計方式，把比較兩個spec 的功能放在 Inventory 裡面，這樣會

吉他如果要新增一個屬性，結果要改三個地方

1. Guitar
2. Inventory,
3. test case

也就是改一個地方就動到全部了

所以設計上把 Guitar 跟吉他的屬性分開，因為客戶搜尋的時候目前是只考慮材質跟製造商

然後 GuitarSpec 裡面加上 matches() 的功能
這樣未來增加一個屬性的時候，只需要改 GuitarSpec 就可以了，其他的功能不會需要修改
