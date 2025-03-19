
ALTER TABLE fct.cart
    DROP CONSTRAINT fk_cart_user,
    ADD CONSTRAINT fk_cart_user FOREIGN KEY (user_id) REFERENCES fct.fct_user(id) ON DELETE CASCADE;

ALTER TABLE fct.frame
    DROP CONSTRAINT fk_frame_finish,
    ADD CONSTRAINT fk_frame_finish FOREIGN KEY (frame_finish_id) REFERENCES fct.frame_finish(id) ON DELETE CASCADE,
    DROP CONSTRAINT fk_frame_type,
    ADD CONSTRAINT fk_frame_type FOREIGN KEY (frame_type_id) REFERENCES fct.frame_type(id) ON DELETE CASCADE;

ALTER TABLE fct.product
    DROP CONSTRAINT fk_product_type,
    ADD CONSTRAINT fk_product_type FOREIGN KEY (product_type_id) REFERENCES fct.product_type(id) ON DELETE CASCADE;

ALTER TABLE fct.product_cart
    DROP CONSTRAINT fk_product,
    ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES fct.product(id) ON DELETE CASCADE,
    DROP CONSTRAINT fk_cart,
    ADD CONSTRAINT fk_cart FOREIGN KEY (cart_id) REFERENCES fct.cart(id) ON DELETE CASCADE;

ALTER TABLE fct.bike
    DROP CONSTRAINT bike_frame_id_fkey,
    ADD CONSTRAINT bike_frame_id_fkey FOREIGN KEY (frame_id) REFERENCES fct.frame(id) ON DELETE CASCADE,
    DROP CONSTRAINT bike_wheel_id_fkey,
    ADD CONSTRAINT bike_wheel_id_fkey FOREIGN KEY (wheel_id) REFERENCES fct.wheel(id) ON DELETE CASCADE,
    DROP CONSTRAINT bike_rim_id_fkey,
    ADD CONSTRAINT bike_rim_id_fkey FOREIGN KEY (rim_id) REFERENCES fct.rim(id) ON DELETE CASCADE,
    DROP CONSTRAINT bike_chain_id_fkey,
    ADD CONSTRAINT bike_chain_id_fkey FOREIGN KEY (chain_id) REFERENCES fct.chain(id) ON DELETE CASCADE,
    DROP CONSTRAINT bike_product_id_fkey,
    ADD CONSTRAINT bike_product_id_fkey FOREIGN KEY (product_id) REFERENCES fct.product(id) ON DELETE CASCADE,
    DROP CONSTRAINT bike_creator_id_fkey,
    ADD CONSTRAINT bike_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES fct.fct_user(id) ON DELETE CASCADE;

ALTER TABLE fct.valid_combinations
    DROP CONSTRAINT valid_combinations_frame_id_fkey,
    ADD CONSTRAINT valid_combinations_frame_id_fkey FOREIGN KEY (frame_id) REFERENCES fct.frame(id) ON DELETE CASCADE,
    DROP CONSTRAINT valid_combinations_wheel_id_fkey,
    ADD CONSTRAINT valid_combinations_wheel_id_fkey FOREIGN KEY (wheel_id) REFERENCES fct.wheel(id) ON DELETE CASCADE,
    DROP CONSTRAINT valid_combinations_rim_id_fkey,
    ADD CONSTRAINT valid_combinations_rim_id_fkey FOREIGN KEY (rim_id) REFERENCES fct.rim(id) ON DELETE CASCADE,
    DROP CONSTRAINT valid_combinations_chain_id_fkey,
    ADD CONSTRAINT valid_combinations_chain_id_fkey FOREIGN KEY (chain_id) REFERENCES fct.chain(id) ON DELETE CASCADE;
