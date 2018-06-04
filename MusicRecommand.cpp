#include "stdafx.h"
#include "leveldb/db.h"
#include "MusicRecommand.h"
#include <string>
#include <iostream>
using namespace std;

MusicDatabase::MusicDatabase(string path) {
	leveldb::Options options;
	options.create_if_missing = true;
	leveldb::Status status = leveldb::DB::Open(options, path, &db);
	assert(status.ok());

}
Status User::SetPasswd(string passwd) {
	passwd_ = passwd;
	return 1;
}
Status MusicDatabase::InsertUser(string user_id, string name, RANK rank, string passwd) {
		db->Put(leveldb::WriteOptions(), user_id, passwd);
		db->Get(leveldb::ReadOptions(), user_id, &value);
		cout << value << endl;
	return 1;
}

