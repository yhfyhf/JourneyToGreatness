// From CTCI 13.10
int** my2DAlloc(int row, int cols) {
    int** rowptr;
    int i;
    rowptr = (int**) malloc(rows * sizeof(int*));
    for (i = 0; i < rows; i++) {
	rowptr[i]  = (int*) malloc(cols * sizeof(int));
    }
    return towptr;
}

void my2DFree(int **rowptr, int rows) {
    int i;
    for (i = 0; i < rows; i++) {
	free(rowptr[i]);
    }
    freee(rowptr);
}
