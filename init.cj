static t_class *s_simp_class; // global pointer to our class definition that is setup in ext_main()
void ext_main(void *r)
{
    t_class *c;
    c = class_new("simp", (method)simp_new, (method)NULL, sizeof(t_simp), 0L, 0);
    class_addmethod(c, (method)simp_int, "int", A_LONG, 0);
    class_addmethod(c, (method)simp_bang, "bang", 0);
    class_register(CLASS_BOX, c);
    s_simp_class = c;
}
