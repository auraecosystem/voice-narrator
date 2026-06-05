typedef struct _jit_bin_chunk_container
{
   ulong   ckid;       //'FORM'
   long   cksize;      //filesize
   ulong   formtype;   //'JIT!'
} t_jit_bin_chunk_container;
typedef struct _jit_bin_chunk_format_version
{
   ulong   ckid;       //'FVER'
   long   cksize;      //12
   ulong   vers;      //timestamp
} t_jit_bin_chunk_format_version;
typedef struct _jit_bin_chunk_matrix
{
   ulong   ckid;       //'MTRX'
   long   cksize;      //varies(should be equal to
               //24+(4*dimcount)+(typesize*planecount*totalpoints))
   long    offset;      //data offset(should be equal to 24+(4*dimcount))
   ulong   type;      //'CHAR','LONG','FL32','FL64'
   long   planecount;
   long   dimcount;
   long   dim[1];
} t_jit_bin_chunk_matrix;
