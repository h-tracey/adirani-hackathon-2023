SELECT 
    `Item name` AS item,
    `Items added to cart` AS cart,
    `Items purchased` AS purchased,
    `Item revenue` as revenue,
     round(`Item revenue` / `Items purchased`,2) as rev_per_purch,
	 round(`Items purchased` / `Items added to cart`,2) as prop_purchased
FROM
    analytics.purchases__cart_purchase_revenue_totals;