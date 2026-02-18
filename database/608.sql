-- Tree Node
SELECT
    f_t.id,
    CASE
        WHEN f_t.p_id IS NULL THEN "Root"
        ELSE
            CASE
                WHEN COUNT(s_t.p_id) > 0 THEN "Inner"
                ELSE "Leaf"
            END
    END AS type
FROM Tree f_t
LEFT JOIN Tree s_t
ON f_t.id == s_t.p_id
GROUP BY f_t.id;
